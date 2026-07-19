#test suite is 100% human designed and implemented

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from dashboard import update_graphs

def test_view_north_post():
    fig1, fig2, fig3 = update_graphs('view', 'north', 'post')
    assert fig1 is not None
    assert fig2 is not None
    assert fig3 is not None

def test_view_east_post():
    fig1, fig2, fig3 = update_graphs('view', 'east', 'post')
    assert fig1 is not None
    assert fig2 is not None
    assert fig3 is not None

def test_view_west_post():
    fig1, fig2, fig3 = update_graphs('view', 'west', 'post')
    assert fig1 is not None
    assert fig2 is not None
    assert fig3 is not None

def test_view_south_post():
    fig1, fig2, fig3 = update_graphs('view', 'south', 'post')
    assert fig1 is not None
    assert fig2 is not None
    assert fig3 is not None

def test_view_all_post():
    fig1, fig2, fig3 = update_graphs('view', 'all', 'post')
    assert fig1 is not None
    assert fig2 is not None
    assert fig3 is not None

def test_view_north_pre():
    fig1, fig2, fig3 = update_graphs('view', 'north', 'pre')
    assert fig1 is not None
    assert fig2 is not None
    assert fig3 is not None

def test_view_east_pre():
    fig1, fig2, fig3 = update_graphs('view', 'east', 'pre')
    assert fig1 is not None
    assert fig2 is not None
    assert fig3 is not None

def test_view_west_pre():
    fig1, fig2, fig3 = update_graphs('view', 'west', 'pre')
    assert fig1 is not None
    assert fig2 is not None
    assert fig3 is not None

def test_view_south_pre():
    fig1, fig2, fig3 = update_graphs('view', 'south', 'pre')
    assert fig1 is not None
    assert fig2 is not None
    assert fig3 is not None

def test_view_all_pre():
    fig1, fig2, fig3 = update_graphs('view', 'all', 'pre')
    assert fig1 is not None
    assert fig2 is not None
    assert fig3 is not None

#system ignores the dataset parameter on purpose when it's on the comapre mode

def test_compare_north():
    fig1, fig2, fig3 = update_graphs('compare', 'north', '_')
    assert fig1 is not None
    assert fig2 is not None
    assert fig3 is not None

def test_compare_east():
    fig1, fig2, fig3 = update_graphs('compare', 'east', '_')
    assert fig1 is not None
    assert fig2 is not None
    assert fig3 is not None

def test_compare_west():
    fig1, fig2, fig3 = update_graphs('compare', 'west', '_')
    assert fig1 is not None
    assert fig2 is not None
    assert fig3 is not None

def test_compare_south():
    fig1, fig2, fig3 = update_graphs('compare', 'south', '_')
    assert fig1 is not None
    assert fig2 is not None
    assert fig3 is not None

def test_compare_all():
    fig1, fig2, fig3 = update_graphs('compare', 'all', '_')
    assert fig1 is not None
    assert fig2 is not None
    assert fig3 is not None