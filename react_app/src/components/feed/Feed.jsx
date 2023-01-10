import Share from '../share/Share'
import Post from '../post/Post'
import './feed.css'
// import { Posts } from '../../dummyData'
import { useEffect, useState } from 'react';

import { useDispatch, useSelector } from 'react-redux';
import BeatLoader from 'react-spinners/BeatLoader';
import { getPosts as listPost } from '../../redux/actions/post_action';

const Feed = () => {
    const dispatch = useDispatch([]);

    useEffect(() => {
        // const paramstring = querystring.stringify(filter);
        dispatch(listPost());
        // setPagination(filter);
    }, []); // [dispatch,filter]

    const list_post = useSelector((state) => state.post_list);
    const { posts, loading, error } = list_post;
    console.log(posts)

    return (
        <div className='feed'>
            <div className='feedWrapper'>
                <Share />
                {/* {Posts.map((p) => (
                    <Post key={p.id} post={p} />
                ))} */}
                {loading ?
                    <BeatLoader
                        className="loading"
                        color={"#000"}
                        loading={loading}
                        // css={override}
                        size={15}
                        margin={2}
                    />
                    : error ? (
                        <h2>{error}</h2>
                    ) : (
                        posts.map((post) => (
                            <Post
                                key={post.id}
                                title={post.title}
                                content={post.content}
                                image_post={post.image_post}
                                user_id={post.user_id}
                                group_id={post.group_id}
                                id={post.id}
                                // postId={post._id}
                            />
                        ))
                    )
                }
            </div>
        </div>
    )
}

export default Feed
