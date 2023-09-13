import {useState} from 'react';
const Search = (props) => {

    const [name,setName] = useState('');
    

    const submit = async(e)=>{
      e.preventDefault();
      const data = {
        "name":name
      }

      const response = await fetch('http://127.0.0.1:8000/ott_search',{
        method:'POST',
        headers:{'Content-Type':'application/json'},
        body:JSON.stringify(data)
      });
      const content = await response.json();
      // console.log(typeof content.name)
      props.setResult(content.name)
    }



  return (
<>
<form onSubmit={submit}>
  <div className='background'>
    <div class="container">

      <div class="row height d-flex justify-content-center align-items-center">

        <div class="col-md-8">

          <div class="search">
            <i class="fa fa-search"></i>
            <input type="text" class="form-control" placeholder="Enter the Name of Movie or Show" onChange={e=>setName(e.target.value)} />
            <button class="btn btn-primary">Search</button>
          </div>

        </div>

      </div>
     
    </div>
    </div>
    </form>
    

    
    </>
  )
}

export default Search