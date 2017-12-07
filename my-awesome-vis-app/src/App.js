// import React, { Component } from 'react';
// import logo from './logo.svg';
// import './App.css';

// class App extends Component {
//   render() {
//     return (
//       <div className="App">
//         <header className="App-header">
//           <img src={logo} className="App-logo" alt="logo" />
//           <h1 className="App-title">Welcome to React</h1>
//         </header>
//         <p className="App-intro">
//           To get started, edit <code>src/App.js</code> and save to reload.
//         </p>
//       </div>
//     );
//   }
// }

// export default App;

import React, { Component } from 'react';
import './App.css';
import '../node_modules/react-vis/dist/style.css';
import { XYPlot, LineSeries, MarkSeries, VerticalBarSeries } from 'react-vis';

class App extends Component {
  render() {
    const series1 = [
      { x: 0, y: 8 },
      { x: 1, y: 5 },
      { x: 2, y: 4 },
      { x: 3, y: 9 },
      { x: 4, y: 1 },
      { x: 5, y: 7 },
      { x: 6, y: 6 },
      { x: 7, y: 3 },
      { x: 8, y: 2 },
      { x: 9, y: 0 }
    ];
    const series2 = [
      { x: 0, y: 2 },
      { x: 1, y: 5 },
      { x: 2, y: 5 },
      { x: 3, y: 9 },
      { x: 4, y: 1 },
      { x: 5, y: 7 },
      { x: 6, y: 7 },
      { x: 7, y: 3 },
      { x: 8, y: 2 },
      { x: 9, y: 3 }
    ];
    const series3 = [
      { x: 0, y: 3 },
      { x: 1, y: 5 },
      { x: 2, y: 7 },
      { x: 3, y: 5 },
      { x: 4, y: 1 },
      { x: 5, y: 7 },
      { x: 6, y: 12 },
      { x: 7, y: 3 },
      { x: 8, y: 3 },
      { x: 9, y: 8 }
    ];
    return (
      <div className="App">
        <XYPlot height={200} width={200}>
          <VerticalBarSeries data={series1} />
          <VerticalBarSeries data={series2} />
          <VerticalBarSeries data={series3} />
        </XYPlot>
        <XYPlot height={200} width={200}>
          <LineSeries data={series1} />
          <LineSeries data={series2} />
          <LineSeries data={series3} />
        </XYPlot>
        <XYPlot height={200} width={200}>
          <MarkSeries data={series1} />
          <MarkSeries data={series2} />
          <MarkSeries data={series3} />
        </XYPlot>
      </div>
    );
  }
}

export default App;