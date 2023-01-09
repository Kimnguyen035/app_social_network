import React, { useState, Component } from 'react'
import './post.css'
import { Users } from '../../dummyData'

// import axios from "axios";

// import { API_URL } from "../constants";

const Post = ({ user_id,group_id,title,content,image_post }) => {
    // const [isLiked, setIsLiked] = useState(false)
    // const [like, setLike] = useState(post.like)
    // const users = Users.filter(u => u.id === post.userId)

    // const likehandler = () => {
    //     setLike(isLiked ? like - 1 : like + 1)
    //     setIsLiked(!isLiked)
    // }

    return (
        <div className='post'>
            <div className='postWrapper'>
                <div className='postTop'>
                    <div className='postTopLeft'>
                        <img src={image_post/*users[0].profilePicture*/} alt='' className='postProfileImg' />
                        <div className='text'>
                            <span className='postUsername'>a{/*users[0].username*/}</span>
                            <span className='postDate'>5 minutes ago</span>{/*post.date*/}
                        </div>
                    </div>
                    <div className='postTopRight'>
                        <span class='material-icons'>more_vert</span>
                        <span class='material-icons'>close</span>
                    </div>
                </div>
                <div className='postCenter'>
                    <span className='postText'>{title}{/*post.desc*/}</span>
                    <img src={image_post/*post.photo*/} alt='' className='postImg' />
                </div>
                <div className='postBottom'>
                    <div className='postBottomLeft'>
                        <img src='/assets/like.png' alt='' className='likeIcon' />{/*onClick={likehandler*/}
                        <img src='/assets/heart.png' alt='' className='likeIcon' />
                        <span className='postLikeCounter'>1 people like it</span>
                    </div>
                    <div className='postBottomRight'>
                        <span className='postCommentText'>1 comments</span>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Post
