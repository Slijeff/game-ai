import {
  Flex,
  Button,
  FormControl,
  FormLabel,
  RadioGroup,
  HStack,
  Radio,
} from "@chakra-ui/react";

export const Menu = ({ setClearSignal, setAiSignal, aiSignal }) => {

  return (
    <Flex direction="column" m={4} justify="space-between" h="20%">
      <FormControl as="fieldset">
        <FormLabel as="legend">Select Agent</FormLabel>
        <RadioGroup defaultValue="Minimax">
          <HStack spacing="24px">
            <Radio value="Minimax">Minimax</Radio>
          </HStack>
        </RadioGroup>
      </FormControl>
      {aiSignal ? (
        <Button colorScheme="teal" isDisabled={true}>
          AI First
        </Button>
      ) : (
        <Button colorScheme="teal" onClick={setAiSignal.on} isDisabled={false}>
          AI First
        </Button>
      )}
      <Button colorScheme="teal" onClick={setClearSignal.toggle}>
        Clear
      </Button>
    </Flex>
  );
};
