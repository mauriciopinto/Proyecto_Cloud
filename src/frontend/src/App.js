import './App.css';
import HomePage from './Pages/Home'
import LoginPage from './Pages/Login'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import UserPage from './Pages/User'
import JobPage from './Pages/Job'
import { useParams } from 'react-router';
import { closeUserSession } from './Services/Account/User';

function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
            <Route exact path="/" element={<HomePage />} />
            <Route path="/login" element={<LoginPage />}/>
            <Route path="/user" element={<UserPage />} />
            <Route path="/job/:jobId" element={<CustomJob/>} />
            <Route path="/logout" element={<LogoutHome/>} />
        </Routes>
      </Router>
    </div>
  );
}

function CustomJob () {
  let params = useParams();
  return <JobPage id={params.jobId} />
}

function LogoutHome () {
  closeUserSession ()
  .then((res) => res)
  .catch(err => err)
  return <HomePage />
}

export default App;
