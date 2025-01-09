const Good = (
  <>
    <CustomComponent />
    <CustomComponent aria-activedescendant={someID} />
    <CustomComponent aria-activedescendant={someID} tabIndex={0} />
    <CustomComponent aria-activedescendant={someID} tabIndex={-1} />
    <div />
    <input />
    <div tabIndex={0} />
    <div aria-activedescendant={someID} tabIndex={0} />
    <div aria-activedescendant={someID} tabIndex="0" />
    <div aria-activedescendant={someID} tabIndex={1} />
    <div aria-activedescendant={someID} tabIndex={-1} />
    <div aria-activedescendant={someID} tabIndex="-1" />
    <input aria-activedescendant={someID} />
    <input aria-activedescendant={someID} tabIndex={0} />
    <input aria-activedescendant={someID} tabIndex={-1} />
  </>
);

const Bad = <div aria-activedescendant={someID} />;
