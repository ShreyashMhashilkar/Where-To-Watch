const Result = (props)=>{
    const {result} = props
    return(
        <div className="background">
            <div className="container">
        
        <div class="card text-center">
  <div class="card-header bg-warning heading">
    <h3>RESULT</h3>
  </div>
  <div class="card-body card-details">
    <p class="card-text"> 
            {
        result.map((res,index)=>
          <h2 className="font-weight-bold" key={index}>{res}</h2>
        )
        
      }</p>
   </div>
   </div>
</div>
        </div>
    )
}

export default Result