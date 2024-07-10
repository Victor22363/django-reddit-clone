import React, { useEffect, useState } from 'react';
import axios from 'axios';

const GetSpecificData = (id) => {
    const [data, setData] = useState([]);
    
    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get(`http://127.0.0.1:8000/api/${id}`);
                setData(response.data);
            } catch (error) {
                console.error('Error fetching data123:', error);
            }
        };

        fetchData();
    }, [id.id]);

    return data;
};
// get all data of the questions
export const GetAllData = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get("http://127.0.0.1:8000/api/");
                //console.log("Got all questions");
                setData(response.data);
            } catch (error) {
                console.error('Error fetching data321:', error);
            }
        };

        fetchData();
    }, []);

    return data;
};
//gets all answers to a given question
export const GetQuestionAnswersData = (id) => {
    const [data, setData] = useState([]);
  
    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get(`http://127.0.0.1:8000/api/filter/${id}`);
                //console.log("Got the question's answers");
                setData(response.data);
            } catch (error) {
                console.error('Error fetching data312:', error);
            }
        };

        fetchData();
    }, []);

    return data;
};


export default GetSpecificData;