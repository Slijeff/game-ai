import flask
import game.gomoku as gmk
import agents.minimax as mm
import heapq
from flask_cors import CORS

app = flask.Flask(__name__)
cors = CORS(app)
gomoku = gmk.Gomoku()
agent = mm.MinimaxAgent()
api = flask.Blueprint('api', __name__)

@api.route('/aiplay')
def aiplay():
    gomoku.set_marker(7, 7, gomoku.player_marker)
    return flask.jsonify({"finished": gomoku.is_game_over(), "board": gomoku.board})


@api.route('/humanplay', methods=['GET'])
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
            score = agent.get_score(move, int(data["depth"]))
            heapq.heappush(heap, (-score, (row, col)))
        airow, aicol = heapq.heappop(heap)[1]
        gomoku.set_marker(airow, aicol, gomoku.player_marker)
        return flask.jsonify({"finished": gomoku.is_game_over(), "board": gomoku.board})


@api.route('/clear')
def clear():
    gomoku.clear_board()
    return flask.jsonify({"board": gomoku.board})

@api.route('/get_board')
def getBoard():
    return flask.jsonify({"board": gomoku.board})

app.register_blueprint(api, url_prefix='/api')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
