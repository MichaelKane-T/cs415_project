import React, {useState, useEffect} from 'react'
import { useNavigate } from "react-router-dom"


const UserView = () => {
    const navigate = useNavigate();
    const [columns, setColumns] = useState([]);
    const [records, setRecords] = useState([]);


    useEffect(() => {
        if (!window.sessionStorage.getItem("auth")) navigate('/unauthorized')
        fetch('http://localhost:8000/users')
        .then(res => res.json())
        .then(data => {
            setColumns(Object.keys(data.users[0]))
            setRecords(data.users)
        })
        .catch(error => console.error(error));
    }, []);

  return (
    <div>
        <h2>Users</h2>
        <table className='table'>
            <thead>
                <tr>
                    {columns.map((c, i) => (
                        <th key={i}>{c.replaceAll("_", " ").toUpperCase()}</th>
                    ))}
                </tr>
            </thead>
            <tbody>
                {
                    records.map((record,i) => (
                        <tr key={i}>
                            <td>{record.user_id}</td>
                            <td>{record.first_name}</td>
                            <td>{record.last_name}</td>
                            <td>{record.email}</td>
                            <td className="hidetext">{record.pass_word}</td>
                            <td>{record.created_date}</td>
                            <td>{record.is_active}</td>
                            <td>{record.last_login}</td>
                        </tr>
                    ))
                }
            </tbody>
        </table>

    </div>
  )
}

export default UserView
