import plotly.graph_objects as go
from plotly.subplots import make_subplots

# --- DATOS ---
meses = ['Jul 25', 'Sep 25', 'Nov 25', 'Ene 26', 'Mar 26']
entidades = [
    'BANCO DE LA NACIÓN ARGENTINA', 'BANCO GALICIA Y BUENOS AIRES', 
    'BANCO SANTANDER ARGENTINA', 'BANCO MACRO', 
    'BBVA ARGENTINA', 'UILO (UALÁ)'
]

titulos_graficos = [f"<b>{e}</b>" for e in entidades]

data_tarj = [[3.2, 3.8, 4.5, 5.2, 5.9], [4.5, 5.1, 6.8, 8.2, 9.1], [4.2, 4.9, 6.5, 7.9, 8.8], 
             [3.8, 4.4, 5.9, 7.1, 7.9], [4.0, 4.7, 6.2, 7.6, 8.4], [9.5, 11.2, 13.8, 15.4, 16.2]]

data_pers = [[4.1, 4.5, 5.2, 6.0, 6.5], [5.2, 6.0, 7.5, 8.8, 9.8], [4.8, 5.5, 7.0, 8.2, 9.2],
             [4.2, 5.0, 6.5, 7.5, 8.5], [4.5, 5.2, 6.8, 8.0, 9.0], [10.5, 12.5, 14.8, 16.5, 18.0]]

COLOR_TARJ = '#2E5A88'
COLOR_PERS = '#95B3D7'
UMBRAL_HISTORICO = 4.2

# --- Hagase los charts! ---
fig = make_subplots(
    rows=3, cols=2, 
    subplot_titles=titulos_graficos,
    vertical_spacing=0.15,
    horizontal_spacing=0.1
)

for i, entidad in enumerate(entidades):
    row, col = (i // 2) + 1, (i % 2) + 1
    
    # Barras Tarjetas
    fig.add_trace(go.Bar(
        x=meses, y=data_tarj[i],
        name='Tarjetas de Crédito',
        marker_color=COLOR_TARJ,
        text=data_tarj[i], texttemplate='%{text}%', textposition='outside',
        textfont=dict(size=10, color='white'),
        legendgroup='tarj', showlegend=(i == 0)
    ), row=row, col=col)
    
    # Barras Personales
    fig.add_trace(go.Bar(
        x=meses, y=data_pers[i],
        name='Créditos Personales',
        marker_color=COLOR_PERS,
        text=data_pers[i], texttemplate='%{text}%', textposition='outside',
        textfont=dict(size=10, color='#1A1A1B'), 
        legendgroup='pers', showlegend=(i == 0)
    ), row=row, col=col)

    # Línea Roja (Promedio Histórico)
    fig.add_hline(
        y=UMBRAL_HISTORICO, 
        line_dash="dash", 
        line_color="red", 
        line_width=1.5,
        row=row, col=col
    )

# --- AJUSTES DE LAYOUT ---
fig.update_layout(
    title=dict(
        text="<b>MONITOREO DE MOROSIDAD POR ENTIDAD Y PRODUCTO</b><br><span style='font-size:14px; color:#95B3D7'>Central de Deudores BCRA - Datos — Promedio Histórico (4.2%) 2025/26</span>",
        x=0.5, y=0.96, xanchor='center'
    ),
    template='plotly_dark',
    width=1100, 
    height=1200, 
    paper_bgcolor='#1A1A1B', 
    plot_bgcolor='#1A1A1B',
    barmode='group',
    margin=dict(t=130, b=80, l=70, r=70),
    legend=dict(
        orientation="h", 
        yanchor="bottom", 
        y=1.02,
        xanchor="center", 
        x=0.5,
        font=dict(size=12)
    )
)

# Ajuste de títulos de subplots
fig.update_annotations(patch=dict(font=dict(size=13, color="white"), yshift=15), selector={'text': titulos_graficos})

# Ejes
fig.update_yaxes(ticksuffix="%", range=[0, 22], gridcolor='#333333')
fig.update_xaxes(tickfont=dict(size=10))

# Nota al pie
fig.add_annotation(
    x=0.5, y=-0.06, xref='paper', yref='paper',
    text="<b>Fuente:</b> Estimaciones basadas en Central de Deudores BCRA.",
    showarrow=False, font=dict(size=11, color="#95B3D7")
)

fig.show()
