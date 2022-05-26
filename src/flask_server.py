import flask
import game.gomoku as gmk
import agents.minimax as mm
import heapq


app = flask.Flask(__name__)
gomoku = gmk.Gomoku()
agent = mm.MinimaxAgent()


@app.route('/')
def home():
    return "Request a position to play"


@app.route('/aiplay', methods=['GET'])
def aiplay():
    data = flask.request.args
    all_moves = gomoku.legal_moves(True)
    heap = []
    for move, row, col in all_moves:
        print("Calculating move for row: {}, col: {}".format(row, col))
        score = agent.get_score(move, data["depth"])
        heapq.heappush(heap, (-score, (row, col)))
    airow, aicol = heapq.heappop(heap)[1]
    gomoku.set_marker(airow, aicol, gomoku.player_marker)
    return {"finished": gomoku.is_game_over(), "board": gomoku.board}


@app.route('/humanplay', methods=['GET'])
def humanplay():
    data = flask.request.args
    gomoku.set_marker(int(data['row']), int(
        data['col']), gomoku.opponent_marker)
    if gomoku.is_game_over():
        return {"finished": True, "board": gomoku.board}
    else:
        all_moves = gomoku.legal_moves(True)
        heap = []
        for move, row, col in all_moves:
            print("Calculating move for row: {}, col: {}".format(row, col))
            score = agent.get_score(move, data["depth"])
            heapq.heappush(heap, (-score, (row, col)))
        airow, aicol = heapq.heappop(heap)[1]
        gomoku.set_marker(airow, aicol, gomoku.player_marker)
        return {"finished": gomoku.is_game_over(), "board": gomoku.board}


@app.route('/clear')
def clear():
    gomoku.clear_board()
    return {"board": gomoku.board}


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
