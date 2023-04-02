import {
	TableContainer,
	Paper,
	Table,
	TableHead,
	TableRow,
	TableCell,
	TableBody,
	CircularProgress,
	Container,
	IconButton,
	Tooltip,
} from "@mui/material";
import axios from "axios";
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { Owner } from "../../models/Owner";
import ReadMoreIcon from "@mui/icons-material/ReadMore";
import EditIcon from "@mui/icons-material/Edit";
import DeleteForeverIcon from "@mui/icons-material/DeleteForever";
import AddIcon from "@mui/icons-material/Add";
import { GlobalURL } from "../../constants";

export const AllOwners = () => {
	const [loading, setLoading] = useState(false);
	const [owners, setOwners] = useState<Owner[]>([]);

	useEffect(() => {
		setLoading(true);
		axios.get(`${GlobalURL}/owners/`)
		  .then(response => {
			setOwners(response.data);
			setLoading(false);
		  })
		  .catch(error => {
			console.error(error);
			setLoading(false);
		  });
	  }, []);

	return (
		<Container>
			<h1>All owners</h1>

			{loading && <CircularProgress />}
			{!loading && owners.length === 0 && <p>No owners found</p>}
			{!loading && (
				<IconButton component={Link} sx={{ mr: 3 }} to={`/owners/add`}>
					<Tooltip title="Add a new owner" arrow>
						<AddIcon color="primary" />
					</Tooltip>
				</IconButton>
			)}
			{!loading && owners.length > 0 && (
				<TableContainer component={Paper}>
					<Table sx={{ minWidth: 650 }} aria-label="simple table">
						<TableHead>
							<TableRow>
								<TableCell>#</TableCell>
								<TableCell align="right">LastName</TableCell>
								<TableCell align="right">FirstName</TableCell>
								<TableCell align="right">CNP</TableCell>
                                <TableCell align="right">Email</TableCell>
                                <TableCell align="right">Address</TableCell>
                            
								<TableCell align="center">Operations</TableCell>
							</TableRow>
						</TableHead>
						<TableBody>
							{owners.map((owner, index) => (
								<TableRow key={owner.id}>
									<TableCell component="th" scope="row">
										{index + 1}
									</TableCell>
                                    <TableCell align="right">{owner.LastName}</TableCell>
                                    <TableCell align="right">{owner.FirstName}</TableCell>
									<TableCell component="th" scope="row">
										<Link to={`/owners/${owner.id}/details`} title="View owner details">
											{owner.CNP}
										</Link>
									</TableCell>
									<TableCell align="right">{owner.Email}</TableCell>
									<TableCell align="right">{owner.Address}</TableCell>
                                    
									<TableCell align="right">

										<IconButton
											component={Link}
											sx={{ mr: 3 }}
											to={`/owners/${owner.id}/details`}>
											<Tooltip title="View owner details" arrow>
												<ReadMoreIcon color="primary" />
											</Tooltip>
										</IconButton>

										<IconButton component={Link} sx={{ mr: 3 }} to={`/owners/${owner.id}/edit`}>
											<Tooltip title="Edit owner details" arrow>
												<EditIcon />
											</Tooltip>
										</IconButton>

										<IconButton component={Link} sx={{ mr: 3 }} to={`/owners/${owner.id}/delete`}>
											<Tooltip title="Delete owner" arrow>
												<DeleteForeverIcon sx={{ color: "red" }} />
											</Tooltip>
										</IconButton>
									</TableCell>
								</TableRow>
							))}
						</TableBody>
					</Table>
				</TableContainer>
			)}
		</Container>
	);
};