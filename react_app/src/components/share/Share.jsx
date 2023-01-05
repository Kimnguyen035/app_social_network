import './share.css'

const Share = () => {

    return (
        <div className='share'>
            <div className='shareWrapper'>
                <div className='shareTop'>
                    <img src='/assets/person/1.jpeg' alt='' className='shareProfileImg' />
                    <input placeholder='What is in your mind Safak?' className='shareInput' />
                </div>
                <hr className='shareHr' />
                <div className='shareBottom'>
                    <div className='shareOptions'>
                        <div className='shareOption'>
                            <span class='material-icons tomato'>perm_media</span>
                            <span className='shareOptionText'>Photo or Video</span>
                        </div>
                        <div className='shareOption'>
                            <span class='material-icons blue'>label</span>
                            <span className='shareOptionText'>Tag</span>
                        </div>
                        <div className='shareOption'>
                            <span class='material-icons green'>room</span>
                            <span className='shareOptionText'>Location</span>
                        </div>
                        <div className='shareOption'>
                            <span class='material-icons goldenrod'>emoji_emotions</span>
                            <span className='shareOptionText'>Fellings</span>
                        </div>
                    </div>
                    <button className='shareButton'>Share</button>
                </div>
            </div>
        </div>
    )
}

export default Share
