import '../styles/App.css'
import '../styles/NavBar.css'
import '../styles/Images.css'

import { useNavigate } from 'react-router-dom';
import React, { useState } from 'react';
import axios from 'axios';





function Reports() {
    const [reports, setReports] = useState([]);
    const [isRunning, setIsRunning] = useState('Peticion not running');
    const apiUrl = "http://3.22.120.139"
    const bucket_url = "https://mia-py2-2s2023-bucket-202001568.s3.us-east-2.amazonaws.com"


    // ...

    const GetReports = async () => {

        try {
            setIsRunning('Peticion running');
            const response = await axios.post(apiUrl + '/reports/all');
            console.log('Respuesta del servidor:', response.data.content)
            setReports(response.data.content);
            setIsRunning('Peticion not running');

        } catch (error) {
            console.error('Error al enviar la URL al servidor:', error);
        }

    }

    // ...

    const navigate = useNavigate();


    const returnHome = () => {
        navigate('/');
    };


    return (

        <>
            <div className="item-0">
                <div className="container-NavB">

                    <div className="item-1-NavB">
                        <button className="button-74" role="button" onClick={returnHome}>Home</button>
                    </div>

                    <div className="item-6-NavB">
                        <button className="button-74" role="button" onClick={GetReports}>Reportes</button>
                    </div>

                </div>
            </div>

            

            <br />
            <br />

            <div className="item-2-images">
            <h1>{isRunning}</h1>

                <center>
                    {reports.map((report, index) => (

                        <img src={`${bucket_url}/${report}`} alt={`Report ${index}`} />

                    ))}

                </center>
            </div>

        </>
    )
}

export default Reports;
