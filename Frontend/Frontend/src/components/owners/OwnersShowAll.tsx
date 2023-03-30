import { useEffect, useState } from "react";
import { GlobalURL } from "../../main";
import { Owner } from "../../models/Owner";

export{}


export const OwnerShowALL = () => {
  const [owners, setOwners]=useState([]);

useEffect(()=>{
  fetch(GlobalURL+"owners/")
  .then((res)=>res.json())
  .then((data)=>setOwners(data));
  
},[]);
 
  return (
    <div className="App">
      <h1>Owners list</h1>
        <table>
          <tr>
            <th>#</th>
            <th>LastName</th>
            <th>FirstName</th>
            <th>CNP</th>
            <th>Email</th>
            <th>Address</th>
            <th>Cars</th>
          </tr>
          {owners.map((owner:Owner,index)=>
          <tr key={index}>
            <td>{index}</td>
            <td>{owner.LastName}</td>
            <td>{owner.FirstName}</td>
            <td>{owner.CNP}</td>
            <td>{owner.Email}</td>
            <td>{owner.Address}</td>
            {/* /<td>{owner.cars}</td> */}
          </tr>)}
        </table>


    </div>
  );
}

