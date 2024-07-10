import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Route, Routes, useParams } from 'react-router-dom';
import Func from './Post'
import Punk from './Look'
import 'bootstrap/dist/css/bootstrap.css'
//import reactLogo from './assets/react.svg'
import './App.css'
import GetSpecificData,{GetAllData} from './GetData.jsx'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div className="App">
      <Router>
          <Routes>
            <Route exact path="/" element={<GetAllDataWrapper/>}/>
            <Route exact path="/:idNum" element={<GetSpecificDataWrapper/>}/>
          </Routes>
      </Router>
    </div>
  )
}

function GetSpecificDataWrapper() {
  const { idNum } = useParams();
  // State to store the fetched data
  const [data, setData] = useState([]);
  const [dataList, setDataList] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        // Fetch specific data
        const response = await fetch(`http://127.0.0.1:8000/api/${idNum}`);
        const dataLocal = await response.json();

        // Fetch and filter data
        const responsefiltered = await fetch(`http://127.0.0.1:8000/api/filter/${dataLocal.id}`);
        const dataListLocal = await responsefiltered.json();

        // Set the filtered data to state
        setData(dataLocal);
        setDataList(dataListLocal);
      } catch (error) {
        // Handle errors
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, [idNum]); // Make sure to include any dependencies that useEffect relies on

  return (
    <div>
      <h1>{data.question_text}</h1>
      {dataList.map(item => (
        <p>{item.text}  :  {item.votes}</p>
      ))}
    </div>
  );
}


function GetAllDataWrapper() {
  const data = GetAllData();
return(
<div>
  {data.map((item) => (
  <div key={item.id}>
    <div>question: {item.question_text}</div>
    <div>votes: {item.votes}</div>

  </div>
    ))}
</div>
);
}



export default App
