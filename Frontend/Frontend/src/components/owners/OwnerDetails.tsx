import { Card, CardActions, CardContent, IconButton } from "@mui/material";
import { Container } from "@mui/system";
import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { Owner } from "../../models/Owner";
import EditIcon from "@mui/icons-material/Edit";
import DeleteForeverIcon from "@mui/icons-material/DeleteForever";
import ArrowBackIcon from "@mui/icons-material/ArrowBack";
import { GlobalURL } from "../../constants";
import { styled } from '@mui/material/styles';
import './OwnerDetails.css';
export const OwnerDetails = () => {
	const { ownerId } = useParams();
	const [owner, setOwner] = useState<Owner>();

	useEffect(() => {
		const fetchOwner = async () => {
			
			const response = await fetch(`${GlobalURL}/owners/${ownerId}`);
			const owner = await response.json();
			setOwner(owner);
		};
		fetchOwner();
	}, [ownerId]);

	return (
		<Container>
			<Card>
				<CardContent>
					<IconButton component={Link} sx={{ mr: 3 }} to={`/owners`}>
						<ArrowBackIcon />
					</IconButton>{" "}
					<h1>Owner Details</h1>
					<p>LastName: {owner?.LastName}</p>
					
                    <p>FirstName: {owner?.FirstName}</p>
					
					<p>CNP: {owner?.CNP}</p>
					
					<p>Email: {owner?.Email}</p>

                    <p>Address: {owner?.Address}</p>
					
					<p>Cars:</p>
					<ol>
						{owner?.cars?.map((car) => (
							<li key={car.id}>
							{[ 
							  `${car.CarBrand} ${car.CarModel}`,
							  <br key="1" />,
							  `Color: ${car.Color}`,
							  <br key="2" />,
							  `Production Year: ${car.ProductionYear}`,
							  <br key="3" />,
							  `Seats: ${car.SeatsNumber}`,
							]}
						  </li>
							
						))}
					</ol>
				</CardContent>
				<CardActions>
					<IconButton component={Link} sx={{ mr: 3 }} to={`/owners/${ownerId}/edit`}>
						<EditIcon />
					</IconButton>

					<IconButton component={Link} sx={{ mr: 3 }} to={`/owners/${ownerId}/delete`}>
						<DeleteForeverIcon sx={{ color: "red" }} />
					</IconButton>
				</CardActions>
			</Card>
		</Container>
	);
};