import {
  Box,
  Button,
  Flex,
  Stack,
  Text,
  useColorModeValue,
} from "@chakra-ui/react";
import { Outlet } from "react-router-dom";
import { useAuth } from "../../hooks/useAuth";
import { ThemeToggler } from "../Theme/ThemeToggler";

export const NavBar = () => {
  const { logout } = useAuth();
  return (
    <Box minHeight="300vh">
      <Flex
        as="nav"
        align="center"
        justify="space-between"
        wrap="wrap"
        padding="1.5rem"
        bg={useColorModeValue("green.300", "green.600")}
        color="white"
      >
        <Text as="h2" fontSize={30} fontWeight="bold">
          NOTE TAKING APP
        </Text>
        <Stack direction="row" align="center" spacing={6}>
          <ThemeToggler size="lg" />
          <Button onClick={logout} colorScheme="red">
            Logout
          </Button>
        </Stack>
      </Flex>
      <Outlet />
    </Box>
  );
};
