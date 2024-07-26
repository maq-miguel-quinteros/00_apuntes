"use client";
import { AppBar, Box, Toolbar, Typography } from '@mui/material';
import React from 'react';

export type NavBarProps = {
	// types...
}

const NavBar: React.FC<NavBarProps> = ({ }) => {
	return (
		<Box sx={{ flexGrow: 1 }}>
			<AppBar position="static">
				<Toolbar>					
					<Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
						Prueba de MUI
					</Typography>
				</Toolbar>
			</AppBar>
		</Box>
	)
};

export default NavBar;
