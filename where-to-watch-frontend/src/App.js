import './App.css';
import Search from './components/Search';
import Result from './components/Result';
import { useState } from 'react';
function App() {
  const [result,setResult] = useState([]);
  console.log(result)
  return (
    <>
    <div className="App">
      <h1 className='heading_name'>WHERE TO WATCH</h1>
      <img src="/image/ott_image2.png" class="img-fluid "  alt="..."></img>
      </div>
      <Search result={result} setResult={setResult}/>
      {/* <h2>{result}</h2> */}
      {/* <Result result={result}/> */}
      <div className='body-background'>
      {
        result.map((res,index)=>
          <h1 className="font-weight-bold" key={index}>{res}</h1>
        )
        
      }
      </div>
      </>
  );
}

export default App;
