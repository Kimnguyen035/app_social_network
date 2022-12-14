from .views import *

class AuthView(ViewSet):
    # ham dang nhap
    def login(self, request):
        data = request.data.copy()
        
        # check input request
        validate = LoginValidate(data=data)
        if not validate.is_valid():
            return validate_error(validate.errors)
        
        username = data[U]
        password = data[P]
        
        # kiem tra ton tai user
        user = self.query_user_exists(username)
        if not user.exists():
            return response_data(status=STATUS['NO_DATA'], message=str(username) + ERROR['not_exists'])
        
        # kiem tra password
        b_password = user.values(P)[0][P]
        if not self.check_passwork(password, b_password):
            return response_data(status=STATUS['FAIL_REQUEST'],message=ERROR['wrong_password'])
        
        # tao token
        a_token, r_token = self.create_token()
        serializer = UserSerializer(user, many=True)
        redis_data = serializer.data[0]
        
        
        user_id = redis_data['id']
        if user_id in cache:
            val_r_token = cache.get(user_id)
            val_a_token = cache.get(val_r_token)
            keys = [val_a_token['token'], val_r_token, user_id]
            cache.delete_many(keys=keys)
            
        # set data redis
        self.set_token_redis(a_token=a_token, r_token=r_token, data=redis_data, user_id=user_id)
        return response_data({
            'access_token': a_token,
            'refresh_token':r_token
        }, message=SUCCESS['login'])

    # ham create user or register
    def register(self, request):
        data = request.data.copy()
        data_save = UserSerializer(data=data)
        if not data_save.is_valid():
            return validate_error(data_save.errors)
        data_save.save()
        return response_data(data_save.data)
        
    # ham lam moi session
    def refresh_token(self, request):
        data = request.data.copy()
        
        validate = RefreshTokenValidate(data=data)
        if not validate.is_valid():
            return validate_error(validate.errors)
        
        # kiem tra refresh token cu
        redis_data = cache.get(data['refresh_token'])
        if redis_data is None:
            return response_data(status=STATUS['INPUT_INVALID'],message=ERROR['refresh_token'])
        user_id = cache.get(redis_data['id'])
        # xoa phien dang nhap cu
        self.delete_token(redis_data['token'], data['refresh_token'], user_id)
        
        # tao token
        a_token, r_token = self.create_token()
        
        # set data redis
        self.set_token_redis(a_token=a_token, r_token=r_token, data=redis_data)
        return response_data({
            'access_token': a_token,
            'refresh_token':r_token
        }, message=SUCCESS['refresh_token'])
        
    # ham dang xuat
    def logout(self, request):
        a_token = request.headers.get("Authorization").replace(TOKEN['type'], '')
        r_token = cache.get(a_token)
        self.delete_token(a_token, r_token)
        return response_data()
        
    
    # duoi day la ham not request
    def hash_password(self, s):
        byte_pwd = s.encode('utf-8')
        my_salt = bcrypt.gensalt()
        pwd_hash = bcrypt.hashpw(byte_pwd, my_salt)
        return pwd_hash
    
    def check_passwork(self, password, b_password):
        return bcrypt.checkpw(password.encode('utf-8'), b_password.encode('utf-8'))
    
    def create_token(self):
        token = {
            'datetime': str(datetime.now()),
            'session': str(uuid.uuid1())
        }
        access_token = self.jwt_encode(data=token, key=TOKEN['public_key'])
        refresh_token = self.jwt_encode(data=token, key=TOKEN['private_key'])
        return access_token, refresh_token
        # return str(access_token).replace("'","").lstrip('b'), str(refresh_token).replace("'","").lstrip('b')
    
    def jwt_encode(self, data, key):
        return jwt.encode(data, key, algorithm=TOKEN['hash'])
    
    def query_user_exists(self, username):
        return User.objects.filter(Q(username=username) | Q(email=username)).filter(deleted_at__isnull=True)
    
    def set_token_redis(self, a_token, r_token, data, user_id):
        data['token'] = a_token
        cache.set(user_id, r_token, timeout=TOKEN['tls_refresh_token'])
        cache.set(a_token, r_token, timeout=TOKEN['tls_access_token'])
        cache.set(r_token, data, timeout=TOKEN['tls_refresh_token'])
    
    # def set_token_redis(self, a_token, r_token, data):
    #     data['token'] = a_token
    #     cache.set(a_token, r_token, timeout=TOKEN['tls_access_token'])
    #     cache.set(r_token, data, timeout=TOKEN['tls_refresh_token'])
        
    def delete_token(self, a_token, r_token, user_id):
        cache.delete(user_id)
        cache.delete(a_token)
        cache.delete(r_token)
        
    # def delete_token(self, a_token, r_token):
    #     cache.delete(a_token)
    #     cache.delete(r_token)
    
    def get_data_token(self, request):
        data = request.headers.get("Authorization").replace(TOKEN['type'], '')
        a = cache.get(data)
        b = cache.get(a)
        c = cache.get(b['id'])
        return response_data({
            'a':a,
            'b':b,
            'c':c
        })
    
    # def get_data_token(self, request):
    #     data = request.headers.get("Authorization").replace(TOKEN['type'], '')
    #     a = cache.get(data)
    #     b = cache.get(a)
    #     return response_data({
    #         'a':a,
    #         'b':b
    #     })
