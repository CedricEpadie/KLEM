import { BrowserRouter, Routes, Route } from 'react-router-dom';
import AcceuilClient from './pages/AcceuilClient';
import CreateClothes from './pages/CreateClothes';


function App() {
  return (
    <div>
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
