import { useState } from 'react'
import './post.css'
import { Users } from '../../dummyData'

const Post = ({post}) => {
    const [isLiked,setIsLiked] = useState(false)
    const [like,setLike] = useState(post.like)
    const users = Users.filter(u=>u.id===post.userId)

    const likehandler = () => {
        setLike(isLiked ? like - 1: like + 1)
        setIsLiked(!isLiked)
    }

    return (
        <div className='post'>
            <div className='postWrapper'>
                <div className='postTop'>
                    <div className='postTopLeft'>
                        <img src={users[0].profilePicture} alt='' className='postProfileImg' />
                        <div className='text'>
                            <span className='postUsername'>{users[0].username}</span>
                            <span className='postDate'>{post.date}</span>
                        </div>
                    </div>
                    <div className='postTopRight'>
                        <span class='material-icons'>more_vert</span>
                        <span class='material-icons'>close</span>
                    </div>
                </div>
                <div className='postCenter'>
                    <span className='postText'>{post.desc}</span>
                    <img src={post.photo} alt='' className='postImg' />
                </div>
                <div className='postBottom'>
                    <div className='postBottomLeft'>
                        <img src='/assets/like.png' onClick={likehandler} alt='' className='likeIcon' />
                        <img src='/assets/heart.png' onClick={likehandler} alt='' className='likeIcon' />
                        <span className='postLikeCounter'>{like} people like it</span>
                    </div>
                    <div className='postBottomRight'>
                        <span className='postCommentText'>{post.comment} comments</span>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Post
