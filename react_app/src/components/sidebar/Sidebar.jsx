import './sidebar.css'
// import { Users } from '../../dummyData'
// import CloseFriend from '../closeFriend/CloseFriend'

const Sidebar = () => {

    return (
        <div className='sidebar'>
            <div className='sidebarWrapper'>
                <ul className='sidebarList'>
                    <li className='sidebarListItem'>
                        <span class='material-icons'>rss_feed</span>
                        <span className='sidebarListItemText'>Feed</span>
                    </li>
                    <li className='sidebarListItem'>
                        <span class='material-icons'>chat</span>
                        <span className='sidebarListItemText'>Chats</span>
                    </li>
                    <li className='sidebarListItem'>
                        <span class='material-icons'>play_circle_filled</span>
                        <span className='sidebarListItemText'>Videos</span>
                    </li>
                    <li className='sidebarListItem'>
                        <span class='material-icons'>group</span>
                        <span className='sidebarListItemText'>Groups</span>
                    </li>
                    <li className='sidebarListItem'>
                        <span class='material-icons'>bookmark</span>
                        <span className='sidebarListItemText'>Bookmark</span>
                    </li>
                    <li className='sidebarListItem'>
                        <span class='material-icons'>help_outline</span>
                        <span className='sidebarListItemText'>Quesions</span>
                    </li>
                    <li className='sidebarListItem'>
                        <span class='material-icons'>work_outline</span>
                        <span className='sidebarListItemText'>Jobs</span>
                    </li>
                    <li className='sidebarListItem'>
                        <span class='material-icons'>event</span>
                        <span className='sidebarListItemText'>Events</span>
                    </li>
                    <li className='sidebarListItem'>
                        <span class='material-icons'>school</span>
                        <span className='sidebarListItemText'>Courses</span>
                    </li>
                </ul>
                {/* <button className='sidebarButton'>Showmore</button>
                <hr className='sidebarHr' />
                <ul className='sidebarFriendList'>
                    {Users.map((u) => (
                        <CloseFriend key={u.id} user={u} />
                    ))}
                </ul> */}
            </div>
        </div>
    )
}

export default Sidebar
