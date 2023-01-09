import Share from '../share/Share'
import Post from '../post/Post'
import './feed.css'
import { Posts } from '../../dummyData'
import { useEffect, useState } from 'react';

import { useDispatch, useSelector } from 'react-redux';
import BeatLoader from 'react-spinners/BeatLoader';
import { getPosts as listPost } from '../../redux/actions/post_action';

const Feed = () => {
    const dispatch = useDispatch([]);

    const getPosts = useSelector((state) => state.getPosts);
    const { posts, loading, error } = getPosts;
    console.log(posts)

    useEffect(() => {
        // const paramstring = querystring.stringify(filter);
        dispatch(listPost());
        // setPagination(filter);
    }, [dispatch]);

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
                                key={post._id}
                                title={post.title}
                                content={post.content}
                                image_post={post.image_post}
                                user_id={post.user_id}
                                group_id={post.group_id}
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
