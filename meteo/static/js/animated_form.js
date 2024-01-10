// https://developer.chrome.com/blog/performant-expand-and-collapse
// https://css-tricks.com/performant-expandable-animations-building-keyframes-on-the-fly/
// https://web.dev/articles/stick-to-compositor-only-properties-and-manage-layer-count

const box = document.querySelector('.box');
const boxContents = document.querySelector('.box__contents');
const boxTitle = document.querySelector('.box__title');
const boxToggleButton = document.querySelector('.button__toggle');
const charts = document.querySelector('.charts');

let expanded = true;
let animate = false;
let collapsed;
let delta;

function activate() {
  box.classList.add('box--active');
  animate = true;
}

function calculateCollapsedScale () {
  const elCollapsed = boxTitle.getBoundingClientRect();
  const elExpanded = box.getBoundingClientRect();
  delta = elExpanded.height - elCollapsed.height;

  collapsed = {
    x: elCollapsed.width / elExpanded.width,
    y: elCollapsed.height / elExpanded.height
  };
}

function expand() {
  if (expanded) {
    return;
  }
  expanded = true;
  box.style.transform = `scale(1, 1)`;
  boxContents.style.transform = `scale(1, 1)`;
  charts.style.transform = `translateY(0px)`;

  if (!animate) {
    return;
  }

  applyAnimation({expand: true});
}

function collapse() {
  if (!expanded) {
    return;
  }
  expanded = false;
  const {x, y } = collapsed;
  const invX = 1 / x;
  const invY = 1 / y;

  box.style.transform = `scale(${x}, ${y})`;
  boxContents.style.transform = `scale(${invX}, ${invY})`;
  charts.style.transform = `translateY(-${delta}px)`;

  if (!animate) {
    return;
  }

  applyAnimation({expand: false});
}

function toggle() {
  !expanded ? expand() : collapse();
}

function addEventListenerOnMenu() {
  boxToggleButton.addEventListener('click', toggle);
}

function applyAnimation({expand}) {
  box.classList.remove('box--expanded');
  box.classList.remove('box--collapsed');
  boxContents.classList.remove('box__contents--expanded');
  boxContents.classList.remove('box__contents--collapsed');
  charts.classList.remove('charts--expanded');
  charts.classList.remove('charts--collapsed');

  window.getComputedStyle(box).transform;

  if (expand) {
    box.classList.add('box--expanded');
    boxContents.classList.add('box__contents--expanded');
    charts.classList.add('charts--expanded');
    return;
  }
  box.classList.add('box--collapsed');
  boxContents.classList.add('box__contents--collapsed');
  charts.classList.add('charts--collapsed');
}

function createEaseAnimation() {
  let boxEase = document.querySelector('.box-ease');
    if (boxEase) {
    return boxEase;
  }

  boxEase = document.createElement('style');
  boxEase.classList.add('box-ease');

  const boxExpandAnimation = [];
  const boxExpandContentsAnimation = [];
  const boxCollapseAnimation = [];
  const boxCollapseContentsAnimation = [];
  const chartsExpandAnimation = [];
  const chartsCollapseAnimation = [];

  for (let i = 0; i <= 100; i++) {
    const step = ease(i/100);

    // Expand animation
    append({
      i,
      step,
      startX: collapsed.x,
      startY: collapsed.y,
      endX: 1,
      endY: 1,
      outerAnimation: boxExpandAnimation,
      innerAnimation: boxExpandContentsAnimation,
    });

    // Collapse animation
    append({
      i,
      step,
      startX: 1,
      startY: 1,
      endX: collapsed.x,
      endY: collapsed.y,
      outerAnimation: boxCollapseAnimation,
      innerAnimation: boxCollapseContentsAnimation,
    });

    // Translate animations
    getTranslate({
      i,
      step,
      delta,
      expandAnimation: chartsExpandAnimation,
      collapsAnimation: chartsCollapseAnimation,
    });
  }

    boxEase.textContent = `
    @keyframes boxExpandAnimation {
      ${boxExpandAnimation.join('')}
    }

    @keyframes boxExpandContentsAnimation {
      ${boxExpandContentsAnimation.join('')}
    }

    @keyframes chartsExpandAnimation {
      ${chartsExpandAnimation.join('')}
    }
    
    @keyframes boxCollapseAnimation {
      ${boxCollapseAnimation.join('')}
    }

    @keyframes boxCollapseContentsAnimation {
      ${boxCollapseContentsAnimation.join('')}
    }

    @keyframes chartsCollapseAnimation {
      ${chartsCollapseAnimation.join('')}
    }`;

  document.head.appendChild(boxEase);
  return boxEase;
}

function append ({
  i,
  step,
  startX, 
  startY, 
  endX, 
  endY, 
  outerAnimation,
  innerAnimation}) {

  const xScale = startX + (endX - startX) * step;
  const yScale = startY + (endY - startY) * step;

  const invScaleX = 1 / xScale;
  const invScaleY = 1 / yScale;

  outerAnimation.push(`
    ${i}% {
      transform: scale(${xScale}, ${yScale});
    }`);

  innerAnimation.push(`
    ${i}% {
      transform: scale(${invScaleX}, ${invScaleY});
    }`);
}

function getTranslate({
  i,
  step,
  delta,
  expandAnimation,
  collapsAnimation,
}) {
  const expandTranslate = -1 * delta + delta * step;
  const collapseTranslate = delta * step;

  expandAnimation.push(`
    ${i}% {
      transform: translateY(${expandTranslate}px);
    }`);

  collapsAnimation.push(`
    ${i}% {
      transform: translateY(${collapseTranslate});
    }`);
}

function clamp (value, min, max) {
  return Math.max(min, Math.min(max, value));
}

function ease (v, pow=4) {
  v = clamp(v, 0, 1);

  return 1 - Math.pow(1 - v, pow);
}

function init() {
  calculateCollapsedScale();
  addEventListenerOnMenu();
  collapse();
  createEaseAnimation();
  activate();
}

init();