import {
  Box,
  AppBar,
  Toolbar,
  IconButton,
  Typography,
  Button,
} from "@mui/material";
import { Link, useLocation } from "react-router-dom";
import SchoolIcon from "@mui/icons-material/School";

import LocalLibraryIcon from "@mui/icons-material/LocalLibrary";

export const AppMenu = () => {
  const location = useLocation();
  const path = location.pathname;

  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static" sx={{ marginBottom: "20px", background: 'linear-gradient(to right, #980cf0, #2557fa)'}}>
        <Toolbar>
          <Link to="/">
            <img
              src="../src/assets/home.png"
              alt="home"
              style={{ marginRight: "16px" }}
			  width={"35px"}
			  height={"35px"}
            />
          </Link>
          <Typography variant="h6" component="div" sx={{ mr: 5 }}>
            App management
          </Typography>
          <Button
            variant={path.startsWith("/owners") ? "outlined" : "text"}
            to="/owners"
            component={Link}
            color="inherit"
            sx={{ mr: 5 }}
            
          >
			<img src="../src/assets/owner.png" 
			alt="owner" 
			style={{ marginRight: '8px' }} 
			width={"25px"}
			height={"25px"}/>
 
            Owners
          </Button>
          <Button
            variant={path.startsWith("/averageprodyear") ? "outlined" : "text"}
            to="/averageprodyear"
            component={Link}
            color="inherit"
            sx={{ mr: 5 }}
      
          >
			<img src="../src/assets/data-management.png" 
			alt="owner" 
			style={{ marginRight: '8px' }} 
			width={"25px"}
			height={"25px"}/>
            Average Production Year - Statistic
          </Button>
        </Toolbar>
      </AppBar>
    </Box>
  );
};
