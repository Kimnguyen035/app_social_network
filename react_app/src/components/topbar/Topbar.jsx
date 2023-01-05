import './topbar.css'

const Topbar = () => {

    return (
        <div className='topbarContainer'>
            <div className='topbarLeft'>
                <div className='logo'>
                    React App
                </div>
            </div>
            <div className='topbarCenter'>
                <div className='searchbar'>
                    <div className='searchIcon'>
                        <span class='material-icons'>search</span>
                    </div>
                    <input placeholder='This is search' type='text' className='searchInput' />
                </div>
            </div>
            <div className='topbarRight'>   
                <div className='topbarLinks'>
                    <span className='topbarLink'>Homepage</span>
                    <span className='topbarLink'>Timeline</span>
                </div>
                <div className='topbarIcons'>
                    <div className='topbarIconItem'>
                        <span class='material-icons'>person</span>
                        <span className='topbarIconBadge'>1</span>
                    </div>
                    <div className='topbarIconItem'>
                        <span class='material-icons'>message</span>
                        <span className='topbarIconBadge'>1</span>
                    </div>
                    <div className='topbarIconItem'>
                        <span class='material-icons'>circle_notifications</span>
                        <span className='topbarIconBadge'>1</span>
                    </div>
                </div>
                <img src='/assets/person/1.jpeg' alt='' className='topbarImg' />
            </div>
        </div>
    )
}

export default Topbar
