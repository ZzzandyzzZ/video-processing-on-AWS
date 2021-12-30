import Navbar from "./Components/Navbar";
import Main from "./Components/Main";
import Video from "./Components/Video";
import Footer from "./Components/Footer";
import { BrowserRouter, Switch, Route } from "react-router-dom";

function App() {
  return (
    <BrowserRouter>
      <Switch>
        <Route
          exact
          path="/"
          render={() => (
            <>
              <Navbar />
              <Main />
              <Footer />
            </>
          )}
        />
        <Route
          exact
          path="/upload"
          render={() => (
            <>
              <Navbar />
              <Footer />
            </>
          )}
        />
        <Route
          exact
          path="/video-tags"
          render={() => (
            <>
              <Navbar />
              <Video />
              <Footer />
            </>
          )}
        />
      </Switch>
    </BrowserRouter>
  );
}

export default App;
