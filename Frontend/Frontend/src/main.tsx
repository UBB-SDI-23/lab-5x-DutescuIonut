import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import "./index.css";

export const GlobalURL="http://127.0.0.1:8000";//This may change in AWS;

import "@fontsource/roboto/300.css";
import "@fontsource/roboto/400.css";
import "@fontsource/roboto/500.css";
import "@fontsource/roboto/700.css";

ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
	<React.StrictMode>
		<App />
	</React.StrictMode>
);