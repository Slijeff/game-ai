import { Board } from "./components/Board";
import { Menu } from "./components/Menu";
import { Center, Flex, useBoolean, Heading } from "@chakra-ui/react";

function App() {
  const [clear, setClearSignal] = useBoolean();
  const [ai, setAiSignal] = useBoolean(false);
  const serverAddr = "api"
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
          <Board clearSignal={clear} aiSignal={ai} setAiSignal={setAiSignal} serverAddr={serverAddr}/>
        </Flex>
      </Center>
      <Center>
        <Menu setClearSignal={setClearSignal} setAiSignal={setAiSignal} aiSignal={ai}/>
      </Center>
    </Flex>
  );
}

export default App;
