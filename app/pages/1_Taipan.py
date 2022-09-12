import streamlit as st

from Main import APP_TITLE


def draw_board(n_square=10):
  board = ["`+" + "-" * n_square + "+`"]
  board.extend("`+" + "_" * n_square + "+`" for _ in range(n_square))
  board.extend("`+" + "-" * n_square + "+`")
  st.markdown("\n".join(board))
  return None


st.markdown("Taipan - the classic Snake game")

tab1, tab2=st.tabs(["Game", "Options"])

with tab1:
  st.write("Game")

  draw_board(n_square=10)


with tab2:
  st.write("Options")
