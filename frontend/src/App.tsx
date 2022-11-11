import './App.css';
import { BrowserRouter, Route, NavLink , Routes} from 'react-router-dom';

import UsersList from './components/UsersList';

function App() {
  return (
    <BrowserRouter>
        <nav>
            <ul>
                <li><NavLink to="/">Home</NavLink></li>
                <li><NavLink to="/users">Users</NavLink></li>
            </ul>
        </nav>
        <Routes>
            <Route path="/users" element={<UsersList />} />
            <Route path="/" element={<h1>My Home Page</h1>} />
        </Routes>
    </BrowserRouter>
  );
}

export default App;
