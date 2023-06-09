
import * as React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { AppHome } from "./components/AppHome";
import { AppMenu } from "./components/AppMenu";
import { AllOwners } from "./components/owners/AllOwners";
import { OwnerAdd } from "./components/owners/OwnerAdd";
import { OwnerDelete } from "./components/owners/OwnerDelete";
import { OwnerDetails } from "./components/owners/OwnerDetails";
import { OwnerUpdate } from "./components/owners/OwnerUpdate";
import { AverageProdYear } from "./components/statistics/AverageProdYear"
function App() {
	return (
		<React.Fragment>
			<Router>
				<AppMenu />

				<Routes>
					<Route path="/" element={<AppHome />} />
					<Route path="/owners" element={<AllOwners />} />
					<Route path="/owners/:ownerId/details" element={<OwnerDetails />} />
					<Route path="/owners/:ownerId/edit" element={<OwnerUpdate />} />
					<Route path="/owners/:ownerId/delete" element={<OwnerDelete />} />
					<Route path="/owners/add" element={<OwnerAdd />} />
					<Route path="/averageprodyear" element={<AverageProdYear/>}></Route>
				</Routes>
			</Router>
		</React.Fragment>
	);
}

export default App;