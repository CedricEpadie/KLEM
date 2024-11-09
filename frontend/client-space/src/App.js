import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { useEffect,useState } from 'react';
import AcceuilClient from './pages/AcceuilClient';
import CreateClothes from './pages/CreateClothes';
import Spinner from './components/Spinner';

function App() {

  const [isLoading, setIsLoading] = useState(true)
    
  useEffect(()=>{
    setTimeout(() => {
      setIsLoading(false)
    }, 1500);
  },[])

  return (
    <div>
      {isLoading && <Spinner />}
      <BrowserRouter>
        <Routes>
          <Route path='/client' element={< AcceuilClient/>} />
          <Route path='/createClothes' element={< CreateClothes/>}/>
          <Route path='*' element={< AcceuilClient/>} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
