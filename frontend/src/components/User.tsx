import { UserDetails} from './types';

function User (props: UserDetails) {
    return (
        <>
            <strong>Username:</strong> {props.user.username}<br />
            <strong>Email:</strong> {props.user.email}<br />
            <hr />
        </>
    );
}
export default User;