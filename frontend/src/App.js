import { Board } from "./components/Board";
import { Menu } from "./components/Menu";
import { Center, Flex, useBoolean, Heading } from "@chakra-ui/react";

function App() {
  const [clear, setClearSignal] = useBoolean();
  const serverAddr = "http://127.0.0.1:5000"
  return (
    <Flex
      direction="row"
      h="100vh"
      w="100vw"
      bg="orange.100"
      justifyContent="center"
    >
      <Center>
        <Flex direction="column">
          <Heading>Gomoku AI</Heading>
          <Board clearSignal={clear} serverAddr={serverAddr}/>
        </Flex>
      </Center>
      <Center>
        <Menu setClearSignal={setClearSignal} />
      </Center>
    </Flex>
  );
}

export default App;
