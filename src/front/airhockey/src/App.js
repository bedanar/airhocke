import BlurBallsBack from "./components/BlurBall";

import { Routes, Route } from "react-router-dom";
import Main from "./pages/Main";
import NotFound from "./pages/NotFound";

function App() {
  return (
    <BlurBallsBack>
      <Routes>
        <Route path="/" element={<Main />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BlurBallsBack>
  );
}

export default App;
