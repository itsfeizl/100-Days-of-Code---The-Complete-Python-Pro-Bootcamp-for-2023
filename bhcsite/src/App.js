import React from "react";

import Home from "./routes/Home";
import About from "./routes/About";
import Members from "./routes/Members";
import Join from "./routes/Join";
import Resources from "./routes/Resources";
import News from "./routes/News";
import Contact from "./routes/Contact";
import Donate from "./routes/Donate";

import { Route, Routes } from "react-router-dom";

function App() {
  return (
    <>
    <Routes>
      <Route path="/" element={<Home />}/>
      <Route path="/about" element={<About />}/>
      <Route path="/members" element={<Members />}/>
      <Route path="/join" element={<Join />}/>
      <Route path="/resources" element={<Resources />}/>
      <Route path="/news" element={<News />}/>
      <Route path="/contact" element={<Contact />}/>
      <Route path="/donate" element={<Donate />}/>
    </Routes>
    </>
  );
}

export default App;
