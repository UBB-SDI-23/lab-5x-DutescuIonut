import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";
import { OwnerShowALL } from "./components/owners/OwnersShowAll";

function App() {
  const [count, setCount] = useState(0);

  return (
    <OwnerShowALL/>
  );
}

export default App;
