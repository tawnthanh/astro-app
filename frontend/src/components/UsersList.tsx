import { useEffect, useState } from 'react';

import UserComponent from './User';
import {User} from './types';


function UsersList () {
    const [users, setUsers] = useState([]);

    useEffect(() => {
        async function fetchData() {
            const response = await fetch('/api/users/');
            const responseData = await response.json();
            setUsers(responseData.users);
        }
        fetchData();
    }, []);

    const userComponents = users.map((user:User) => <UserComponent key={user.id} user={user} />)
    return (
        <>
            <h1>User List: </h1>
            {userComponents}
        </>
        );
}

export default UsersList;