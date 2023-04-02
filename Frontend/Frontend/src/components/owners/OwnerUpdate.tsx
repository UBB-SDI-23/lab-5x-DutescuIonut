import {
  Button,
  Card,
  CardActions,
  CardContent,
  CircularProgress,
  Container,
  IconButton,
  TextField,
} from "@mui/material";
import { useEffect, useState } from "react";
import { Link, useNavigate, useParams } from "react-router-dom";
import { Owner } from "../../models/Owner";
import ArrowBackIcon from "@mui/icons-material/ArrowBack";
import axios from "axios";
import { GlobalURL } from "../../constants";

export const OwnerUpdate = () => {
  const navigate = useNavigate();
  const { ownerId } = useParams();

  const [loading, setLoading] = useState(true);
  const [owner, setOwner] = useState<Owner | null>(null);

  useEffect(() => {
    const fetchOwner = async () => {
      try {
        const response = await axios.get<Owner>(
          `${GlobalURL}/owners/${ownerId}`
        );
        setOwner(response.data);
      } catch (error) {
        console.log(error);
      } finally {
        setLoading(false);
      }
    };
    fetchOwner();
  }, [ownerId]);

  const updateOwner = async (event: { preventDefault: () => void }) => {
    event.preventDefault();
    try {
      await axios.put(`${GlobalURL}/owners/${ownerId}`, owner);
      navigate(`/owners/`);
    } catch (error) {
      console.log(error);
    }
  };


  return (
    <Container>
      {loading && <CircularProgress />}

      {!loading && !owner && <div>Owner not found</div>}

      {!loading && owner && (
        <Card>
          <CardContent>
            <IconButton
              component={Link}
              sx={{ mr: 3 }}
              to={`/owners/`}
            >
              <ArrowBackIcon />
            </IconButton>{" "}
            <form onSubmit={updateOwner}>
              <TextField
                value={owner.FirstName}
                id="first_name"
                label="First name"
                variant="outlined"
                fullWidth
                sx={{ mb: 2 }}
                onChange={(event) =>
                  setOwner({ ...owner, FirstName: event.target.value })
                }
              />
              <TextField
                value={owner.LastName}
                id="last_name"
                label="Last name"
                variant="outlined"
                fullWidth
                sx={{ mb: 2 }}
                onChange={(event) =>
                  setOwner({ ...owner, LastName: event.target.value })
                }
              />

              <TextField
                value={owner.CNP}
                id="cnp"
                label="CNP"
                variant="outlined"
                fullWidth
                sx={{ mb: 2 }}
                onChange={(event) =>
                  setOwner({ ...owner, CNP: event.target.value })
                }
              />

              <TextField
                value={owner.Email}
                id="email"
                label="Email"
                variant="outlined"
                fullWidth
                sx={{ mb: 2 }}
                onChange={(event) =>
                  setOwner({ ...owner, Email: event.target.value })
                }
              />
              <TextField
                value={owner.Address}
                id="address"
                label="Address"
                variant="outlined"
                fullWidth
                sx={{ mb: 2 }}
                onChange={(event) =>
                  setOwner({ ...owner, Address: event.target.value })
                }
              />

              <Button type="submit">Update Owner</Button>
            </form>
          </CardContent>
          <CardActions></CardActions>
        </Card>
      )}
    </Container>
  );
};
