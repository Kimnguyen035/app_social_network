import './home.css';
import Sidebar from '../components/sidebar/Sidebar'
import Topbar from '../components/topbar/Topbar'
import Feed from '../components/feed/Feed'

const Home = () => {
  return (
    <>
      <Topbar />
      <div className="homContainer">
        <Sidebar />
        <Feed />
      </div>
    </>
  );
}

export default Home;
