const menuTitle = document.querySelector('.menu__title');
const menu = document.querySelector('.menu');
const menuContents = document.querySelector('.menu__contents');
const menuToggleButton = document.querySelector('.button__toggle');
const charts = document.querySelector('.charts');

let expanded = true;
let animate = false;
let collapsed;
let delta;

function activate() {
  menu.classList.add('menu--active');
  animate = true;
}

function calculateCollapsedScale () {
  const elCollapsed = menuTitle.getBoundingClientRect();
  const elExpanded = menu.getBoundingClientRect();
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
  menu.style.transform = `scale(1, 1)`;
  menuContents.style.transform = `scale(1, 1)`;
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

  menu.style.transform = `scale(${x}, ${y})`;
  menuContents.style.transform = `scale(${invX}, ${invY})`;
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
  menuToggleButton.addEventListener('click', toggle);
}

function applyAnimation({expand}) {
  menu.classList.remove('menu--expanded');
  menu.classList.remove('menu--collapsed');
  menuContents.classList.remove('menu__contents--expanded');
  menuContents.classList.remove('menu__contents--collapsed');
  charts.classList.remove('charts--expanded');
  charts.classList.remove('charts--collapsed');

  window.getComputedStyle(menu).transform;

  if (expand) {
    menu.classList.add('menu--expanded');
    menuContents.classList.add('menu__contents--expanded');
    charts.classList.add('charts--expanded');
    return;
  }
  menu.classList.add('menu--collapsed');
  menuContents.classList.add('menu__contents--collapsed');
  charts.classList.add('charts--collapsed');
}

function createEaseAnimation() {
  let menuEase = document.querySelector('.menu-ease');
    if (menuEase) {
    return menuEase;
  }

  menuEase = document.createElement('style');
  menuEase.classList.add('menu-ease');

  const menuExpandAnimation = [];
  const menuExpandContentsAnimation = [];
  const menuCollapseAnimation = [];
  const menuCollapseContentsAnimation = [];
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
      outerAnimation: menuExpandAnimation,
      innerAnimation: menuExpandContentsAnimation,
    });

    // Collapse animation
    append({
      i,
      step,
      startX: 1,
      startY: 1,
      endX: collapsed.x,
      endY: collapsed.y,
      outerAnimation: menuCollapseAnimation,
      innerAnimation: menuCollapseContentsAnimation,
    });

    // Both translate animations
    getTranslate({
      i,
      step,
      delta,
      expandAnimation: chartsExpandAnimation,
      collapsAnimation: chartsCollapseAnimation,
    });
  }

    menuEase.textContent = `
    @keyframes menuExpandAnimation {
      ${menuExpandAnimation.join('')}
    }

    @keyframes menuExpandContentsAnimation {
      ${menuExpandContentsAnimation.join('')}
    }

    @keyframes chartsExpandAnimation {
      ${chartsExpandAnimation.join('')}
    }
    
    @keyframes menuCollapseAnimation {
      ${menuCollapseAnimation.join('')}
    }

    @keyframes menuCollapseContentsAnimation {
      ${menuCollapseContentsAnimation.join('')}
    }

    @keyframes chartsCollapseAnimation {
      ${chartsCollapseAnimation.join('')}
    }`;


  document.head.appendChild(menuEase);
  return menuEase;
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