import streamlit as st
import pandas as pd
import numpy as np
import sympy as sy
from matplotlib import pyplot as plt
from sympy.plotting.plot import MatplotlibBackend, Plot
from sympy.plotting import plot3d,plot3d_parametric_line
import plotly as ply
import plotly.express as ex
import plotly.graph_objects as gro
from plotly.subplots import make_subplots
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title='Cálculo III', page_icon=':pencil2:', layout='wide', initial_sidebar_state='collapsed')




st.markdown('''

<style>
[data-testid="collapsedControl"] {
        display: none
    }

#MainMenu, header, footer {visibility: hidden;}
''', unsafe_allow_html=True)

if st.button('Regresar'):
    st.write('Regresando...')
    switch_page('Main')

def taylor_derivative(f, var, n):
    """
    This function calculates the nth derivative of a given function f with respect to a variable var at a point x0 using
    Taylor series.

    :param f: The function for which we want to calculate the nth derivative
    :param var: The variable with respect to which the derivative is being taken
    :param n: n is the order of the derivative to be calculated using Taylor series expansion
    :return: The function `taylor_derivative` returns the nth derivative of the function `f` with respect to the variable
    `var` evaluated at `x0`.
    """
    df = f
    for _ in range(n):
        df = sy.diff(df, var)

    return df

def get_sympy_subplots(plot:Plot):
    """
    It takes a plot object and returns a matplotlib figure object

    :param plot: The plot object to be rendered
    :type plot: Plot
    :return: A matplotlib figure object.
    """
    backend = MatplotlibBackend(plot)

    backend.process_series()
    backend.fig.tight_layout()
    return backend.plt


st.subheader('Método')
xxs = st.text_input('Ingrese la función $f(x)$: ',value='(x - 1)**2')


fx = sy.parse_expr(xxs,transformations='all')
intstrr = ''

symb = st.selectbox('Variable a considerar: ',list(fx.free_symbols))
order = st.number_input('Orden de la derivada',1,100,value=1)
method = taylor_derivative(fx,symb,int(order))

st.latex(r'\frac{\partial f}{\partial ' + str(symb) +'}'+sy.latex(fx)+' = ' + sy.latex(str(method)))


if len(fx.free_symbols)<= 2:
    if len(fx.free_symbols) == 1:
        func = sy.lambdify(list(fx.free_symbols),fx)
        plo = gro.Figure()
        plo.add_trace(gro.Scatter(x=np.linspace(-10,10,1000),y=func(np.linspace(-10,10,1000))))
        st.plotly_chart(plo)
        p =sy.plot(fx,show=False)
        pl = get_sympy_subplots(p)

        st.pyplot(pl)

    if  len(fx.free_symbols) == 2:
        func = sy.lambdify(list(fx.free_symbols),fx)
        plo = gro.Figure()
        ran = np.linspace(-10,10,100)
        su = [[func(ran[xs],ran[ys]) for xs in range (0,len(ran)) ] for ys in range(0,len(ran))]
        plo.add_trace(gro.Surface(z=su))
        st.plotly_chart(plo)
        p =plot3d(fx,show=False)
        pl = get_sympy_subplots(p)

        st.pyplot(pl)




