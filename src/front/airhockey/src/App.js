import { Routes, Route } from "react-router-dom";
import Main from "./pages/Main";
import NotFound from "./pages/NotFound";
import Layout from "./components/Layout";
import ProfilePage from "./pages/Profile";

function App() {
  return (
    <Layout>
        <Routes>
          <Route path="/" element={<Main />} />
          <Route path="/user" element={<ProfilePage />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
    </Layout>
  );
}

export default App;
