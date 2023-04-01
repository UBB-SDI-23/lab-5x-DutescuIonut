import { Button, Card, CardActions, CardContent, IconButton, TextField } from "@mui/material";
import { Container } from "@mui/system";
import { useEffect, useState } from "react";
import { Link, useNavigate, useParams } from "react-router-dom";

import { Owner } from "../../models/Owner";
import EditIcon from "@mui/icons-material/Edit";
import DeleteForeverIcon from "@mui/icons-material/DeleteForever";
import ArrowBackIcon from "@mui/icons-material/ArrowBack";
import axios from "axios";
import { GlobalURL } from "../../constants";

export const OwnerAdd = () => {
	const navigate = useNavigate();

	const [owner, setOwner] = useState<Owner>({
		LastName: "",
        FirstName:"",
		CNP: "",
        Email: "",
        Address: "",
	});

	const addOwner = async (event: { preventDefault: () => void }) => {
		event.preventDefault();
		try {
			await axios.post(`${GlobalURL}/owners/`, owner);
			navigate("/owners");
		} catch (error) {
			console.log(error);
		}
	};

	return (
		<Container>
			<Card>
				<CardContent>
					<IconButton component={Link} sx={{ mr: 3 }} to={`/owners`}>
						<ArrowBackIcon />
					</IconButton>{" "}
					<form onSubmit={addOwner}>
						<TextField
							id="LastName"
							label="LastName"
							variant="outlined"
							fullWidth
							sx={{ mb: 2 }}
							onChange={(event: React.ChangeEvent<HTMLInputElement>)=> setOwner({ ...owner, LastName: event.target.value })}
						/>
                        <TextField
							id="FirstName"
							label="FirstName"
							variant="outlined"
							fullWidth
							sx={{ mb: 2 }}
							onChange={(event: React.ChangeEvent<HTMLInputElement>) => setOwner({ ...owner, FirstName: event.target.value })}
						/>
						<TextField
							id="CNP"
							label="CNP"
							variant="outlined"
							fullWidth
							sx={{ mb: 2 }}
							onChange={(event: React.ChangeEvent<HTMLInputElement>) => setOwner({ ...owner, CNP: event.target.value })}
						/>
						 <TextField
							id="Email"
							label="Email"
							variant="outlined"
							fullWidth
							sx={{ mb: 2 }}
							onChange={(event: React.ChangeEvent<HTMLInputElement>) => setOwner({ ...owner, Email: event.target.value })}
						/>
						 <TextField
							id="Address"
							label="Address"
							variant="outlined"
							fullWidth
							sx={{ mb: 2 }}
							onChange={(event: React.ChangeEvent<HTMLInputElement>) => setOwner({ ...owner, Address: event.target.value })}
						/>

						<Button type="submit">Add Owner</Button>
					</form>
				</CardContent>
				<CardActions></CardActions>
			</Card>
		</Container>
	);
};