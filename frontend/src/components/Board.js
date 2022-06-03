import { useCallback, useEffect, useMemo, useRef } from "react";
import { FieldBoardObject, SVGBoard } from "wgo";
import { useBoolean, useToast } from "@chakra-ui/react";

export const Board = ({ clearSignal, aiSignal ,setAiSignal, serverAddr }) => {
  const boardContainerRef = useRef();
  const stones = useRef([]);
  const board = useMemo(() => {
    return new SVGBoard(document.createElement("div"), {
      size: 15,
      width: 700,
      coordinates: true,
    });
  }, []);
  const matrix = useMemo(() => {
    const m = [];
    for (let i = 0; i < board.getSize() * board.getSize(); i++) {
      m[i] = "_";
    }
    return m;
  }, [board]);

  const calBoard = useRef([]);
  const [isEmpty, setNotEmpty] = useBoolean(true);
  const DEPTH = 1;
  const toast = useToast();
  const startingToast = useRef();

  const fetchPlay = useCallback(
    async (row, col) => {
      if (isEmpty) {
        calBoard.current = matrix;
        setNotEmpty.toggle();
      }
      const loadingToast = toast({
        title: "Calculating...",
        description: "This might take a while",
        duration: null,
        position: "top",
      });
      const data = await fetch(
        `${serverAddr}/humanplay?row=${row}&col=${col}&depth=${DEPTH}`
      );
      toast.close(loadingToast);

      const json = await data.json();
      if (json["finished"] === true) {
        toast({
          title: "Game Complete",
          duration: null,
          position: "top",
          isClosable: true,
          status: "warning"
        });
      }
      const resBoard = json["board"];
      for (let i = 0; i < board.getSize(); i++) {
        for (let j = 0; j < board.getSize(); j++) {
          if (
            resBoard[i][j] === "x" &&
            calBoard.current[j + i * board.getSize()] !== "x"
          ) {
            stones.current.push(j + i * board.getSize());
            board.addObject(new FieldBoardObject(aiSignal ? "B" : "W", j, i));
          }
        }
      }
      calBoard.current = [].concat(...resBoard);
    },
    [board, isEmpty, matrix, setNotEmpty, serverAddr, toast, aiSignal]
  );

  const fetchAIPlay = useCallback(async() => {
    toast.closeAll();
    const data = await fetch(`${serverAddr}/aiplay`);
    const json = await data.json();
    const resBoard = json["board"];
    for (let i = 0; i < board.getSize(); i++) {
      for (let j = 0; j < board.getSize(); j++) {
        if (
          resBoard[i][j] === "x" &&
          calBoard.current[j + i * board.getSize()] !== "x"
        ) {
          stones.current.push(j + i * board.getSize());
          board.addObject(new FieldBoardObject("B", j, i));
        }
      }
    }
    calBoard.current = [].concat(...resBoard);
  }, [board, serverAddr, toast]);

  // Handles rendering the board
  useEffect(() => {
    startingToast.current = toast({
      title: "Hint",
      duration: null,
      position: "top",
      description: "Drop a piece to get started, or click AI First"
    });
    const elem = board.element;
    const parent = boardContainerRef.current;
    parent.appendChild(elem);

    return () => {
      parent.removeChild(elem);
    };
  }, [board, toast]);

  // Handles user click on the board
  useEffect(() => {
    const handler = (ev, pos) => {
      toast.closeAll();
      // If current position is not empty, do nothing
      if (stones.current.includes(pos.x + pos.y * board.getSize())) return;
      fetchPlay(pos.y, pos.x).catch((error) => {
        console.log(error);
      });
      board.addObject(new FieldBoardObject(aiSignal ? "W" : "B", pos.x, pos.y));
      stones.current.push(pos.x + pos.y * board.getSize());
    };
    board.on("click", handler);
    return () => {
      board.off("click", handler);
    };
  }, [board, fetchPlay, aiSignal, toast]);

  // Handles clear button
  useEffect(() => {
    board.removeAllObjects();
    board.redraw();
    stones.current = [];
    calBoard.current = [];
    setAiSignal.off();
    fetch(`${serverAddr}/clear`);
  }, [board, clearSignal, serverAddr, setAiSignal]);

  // Handles ai first button
  useEffect(() => {
    console.log(aiSignal);
    if (aiSignal === false) {
      return;
    }
    fetchAIPlay();
  }, [board, aiSignal, serverAddr, fetchAIPlay])

  return (
    <div>
      <div id={"parent"} ref={boardContainerRef} />
    </div>
  );
};
