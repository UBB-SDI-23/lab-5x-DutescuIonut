// import {
// 	TableContainer,
// 	Paper,
// 	Table,
// 	TableHead,
// 	TableRow,
// 	TableCell,
// 	TableBody,
// 	CircularProgress,
// 	Container,
// 	IconButton,
// 	Tooltip,
// } from "@mui/material";
// import axios from "axios";
// import { useEffect, useState } from "react";
// import { Link } from "react-router-dom";
// import { Owner } from "../../models/Owner";
// import ReadMoreIcon from "@mui/icons-material/ReadMore";
// import EditIcon from "@mui/icons-material/Edit";
// import DeleteForeverIcon from "@mui/icons-material/DeleteForever";
// import AddIcon from "@mui/icons-material/Add";
// import { GlobalURL } from "../../main";

// export const AverageProdYear = () => {
// 	const [loading, setLoading] = useState(false);
// 	const [avg, setAvg] = useState<[]>([]);

// 	useEffect(() => {
// 		setLoading(true);
// 		axios.get(`${GlobalURL}/averageprodyear/`)
// 		  .then(response => {
// 			setAvg(response.data);
// 			setLoading(false);
// 		  })
// 		  .catch(error => {
// 			console.error(error);
// 			setLoading(false);
// 		  });
// 	  }, []);

// 	return (
// 		<Container>
// 			<h1>Average Production Year Carbrands</h1>
//             <p>here we have carbrands ordered by average production year of their existent cars</p>
// 			{loading && <CircularProgress />}
// 			{!loading && avg.length === 0 && <p>No owners found</p>}
// 			{!loading && (
// 				<IconButton component={Link} sx={{ mr: 3 }} to={`/owners/add`}>
// 					<Tooltip title="Add a new owner" arrow>
// 						<AddIcon color="primary" />
// 					</Tooltip>
// 				</IconButton>
// 			)}
// 			{!loading && avg.length > 0 && (
// 				<TableContainer component={Paper}>
// 					<Table sx={{ minWidth: 650 }} aria-label="simple table">
// 						<TableHead>
// 							<TableRow>
// 								<TableCell>#</TableCell>
// 								<TableCell align="right">CarBrand</TableCell>
// 								<TableCell align="right">Avg_Production_Year</TableCell>
// 								<TableCell align="right">Car_Count</TableCell>
                               
                            
// 								<TableCell align="center">Operations</TableCell>
// 							</TableRow>
// 						</TableHead>
// 						<TableBody>
// 							{avg.map((avg, index) => (
// 								<TableRow key={}>
// 									<TableCell component="th" scope="row">
// 										{index + 1}
// 									</TableCell>
//                                     <TableCell align="right">{}</TableCell>
//                                     <TableCell align="right">{owner.FirstName}</TableCell>
// 									<TableCell component="th" scope="row">
// 										<Link to={`/owners/${owner.id}/details`} title="View owner details">
// 											{owner.CNP}
// 										</Link>
// 									</TableCell>
// 									<TableCell align="right">{owner.Email}</TableCell>
// 									<TableCell align="right">{owner.Address}</TableCell>
                                    
// 									<TableCell align="right">

// 										<IconButton
// 											component={Link}
// 											sx={{ mr: 3 }}
// 											to={`/owners/${owner.id}/details`}>
// 											<Tooltip title="View owner details" arrow>
// 												<ReadMoreIcon color="primary" />
// 											</Tooltip>
// 										</IconButton>

// 										<IconButton component={Link} sx={{ mr: 3 }} to={`/owners/${owner.id}/edit`}>
// 											<EditIcon />
// 										</IconButton>

// 										<IconButton component={Link} sx={{ mr: 3 }} to={`/owners/${owner.id}/delete`}>
// 											<DeleteForeverIcon sx={{ color: "red" }} />
// 										</IconButton>
// 									</TableCell>
// 								</TableRow>
// 							))}
// 						</TableBody>
// 					</Table>
// 				</TableContainer>
// 			)}
// 		</Container>
// 	);
// };