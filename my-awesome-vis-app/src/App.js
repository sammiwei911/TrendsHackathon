import React, { Component } from 'react';
import './App.css';
import '../node_modules/react-vis/dist/style.css';
import {
  XYPlot,
  LineMarkSeries,
  MarkSeries,
  VerticalGridLines,
  HorizontalGridLines,
  XAxis,
  YAxis,
  DiscreteColorLegend
 } from 'react-vis';
import axios from 'axios';
import * as _ from 'lodash';
import { Button, Grid, Label, Header } from 'semantic-ui-react';
import 'semantic-ui-css/semantic.min.css';


class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      chartData:[],
      measurements: {},
      dataReady: false
    };
    this.chartData = [];
    this.setDataReadyOnce = _.once(this.setDataReady);
  }

  componentDidMount() {
    let tileNumber = 0;
    while(tileNumber < 4){
      this.getChartData();
      tileNumber++;
    }
    // this.setClicks();
    // this.incrementClicks();
    // this.resetClicks();
  }
  setDataReady(){
    this.setState({
      dataReady: true
    })
  }

  getChartData() {
    axios.get('http://127.0.0.1:5000/generate_chart').then(({data}) => {
      data['lengendData'] = this.parseMetaDataLegend(data.metadata.entities);
      this.chartData.push(data);
      if(this.chartData.length === 4){
        this.setDataReadyOnce();
      }
    });
  }

  setClicks (){
    axios.post('http://127.0.0.1:5000/set_clicks', {
      "entities": { "Napa, CA": 100, "Alameda, CA": 72 },
      "viz_types": { "single_entity_spend_pc_py": 100 },
      "y": { "administrative": 100, "police": 59 },
      "z": { "income_per_capita": 105, "population": 46 }
    })
    .then(response => {
      this.setState({ measurements: response });
    })
  }

  incrementClicks (metadata){
    axios.post('http://127.0.0.1:5000/increment_clicks', metadata);
  }

  resetClicks () {
    axios.post('http://127.0.0.1:5000/reset_clicks')
      .then(response => {
        this.setState({ measurements: response});
      })
  }

  parseMetaDataLegend(entities){
    const lengendItems = [];
    entities.map((entity) =>{
      const lengendItem = { title: entity };
      lengendItems.push(lengendItem);
    })
    return lengendItems;
  }
  
  parseTitleData(title){
    return title.split('_').map(function capitalize(part) {
      return part.charAt(0).toUpperCase() + part.slice(1);
    }).join(' ');;
  }

  parseHeader({viz_type, z}){
    if (viz_type === 'single_entity_spend_pc_py'){
      return 'Spend Per Capita';
    } else if (viz_type === 'single_entity_v_others_pc_py'){
      return 'Entity Per Capita';
    } else if (viz_type === 'all_entity_spend_py_sized_by_z'){
      return 'All Entity Spend By ' + this.parseTitleData(z);
    } else {
      return 'All Entity Spend By Spend';
    }
  }

  render() {
    return (
      <div className="App">
        <Grid columns={4} divided style={{ 'margin': '30px' }}>
          <Grid.Row>
          {
            this.chartData.map((responseData, index) => {
              if (['single_entity_spend_pc_py', 'single_entity_v_others_pc_py'].includes(responseData.metadata.viz_type)) {
                return (
                  <Grid.Column>
                    <Header size='medium'>{this.parseHeader(responseData.metadata)}</Header>
                    <Label style={{ 'marginBottom': '50px' }} as='a' color='yellow' tag>{this.parseTitleData(responseData.metadata.y)}</Label>
                  <XYPlot height={350} width={350}>
                    <VerticalGridLines />
                    <HorizontalGridLines />
                    <XAxis />
                    <YAxis />
                    <DiscreteColorLegend items={responseData.lengendData} orientation='horizontal' />
                    {
                      Object.keys(responseData.data).map(function (key, index) {
                        const entityData = responseData.data[key];
                        return <LineMarkSeries
                                key={`line-chart-${index}`}
                                data={entityData}
                                style={{ line: { stroke: "blue" }, mark: { stroke: "red" } }}
                              />
                      })
                    }
                  </XYPlot>
                  <Button color='red'
                    content='Like'
                    icon='heart'
                    style={{ 'marginTop': '100px' }}
                    onClick={() => this.incrementClicks(responseData.metadata)}>
                    Like
                  </Button>
                  </Grid.Column>
                )
              }else{
                return (
                  <Grid.Column>
                    <Header size='medium'>{this.parseHeader(responseData.metadata)}</Header>
                    <Label style={{ 'marginBottom': '50px' }} as='a' color='teal' tag>{this.parseTitleData(responseData.metadata.y)}</Label>
                  <XYPlot height={350} width={350}>
                    <VerticalGridLines />
                    <HorizontalGridLines />
                    <XAxis />
                    <YAxis />
                    <DiscreteColorLegend items={responseData.lengendData} orientation='horizontal' />
                    {
                      Object.keys(responseData.data).map(function (key, index) {
                        const entityData = responseData.data[key];
                        return <MarkSeries
                                opacity={80}
                                sizeRange={[12, 20]}
                                key={`bubble-chart-${index}`}
                                opacity='0.7'
                                data={entityData} />
                      })
                    }
                  </XYPlot>
                  <Button
                    color='red'
                    content='Like'
                    icon='heart'
                    style={{ 'marginTop':'100px'}} onClick={() => this.incrementClicks(responseData.metadata)}>
                    Like
                  </Button>
                  </Grid.Column>
                )
              }
            })
          }
          </Grid.Row>
        </Grid>
        <Button onClick={() => this.resetClicks()}> Reset Values</Button>
      </div>
    );
  }
}

export default App;