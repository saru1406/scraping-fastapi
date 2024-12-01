import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Index from './Pages/Index';
import ChatPage from './Pages/Chat';
import CustomPage from './Pages/Custom';
import CustomIndexPage from './Pages/CustomIndex';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/index" element={<Index />} />
        <Route path="/" element={<ChatPage />} />
        <Route path="/custom" element={<CustomPage />} />
        <Route path="/custom-index" element={<CustomIndexPage />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;