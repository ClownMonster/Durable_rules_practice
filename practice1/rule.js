var d = require('durable');

d.ruleset('animal', function() {
    whenAll: {
        first = m.predicate == 'eats' && m.object == 'flies' 
        m.predicate == 'lives' && m.object == 'water' && m.subject == first.subject
    }
    run: assert({ subject: first.subject, predicate: 'is', object: 'frog' })

    whenAll: {
        first = m.predicate == 'eats' && m.object == 'flies' 
        m.predicate == 'lives' && m.object == 'land' && m.subject == first.subject
    }
    run: assert({ subject: first.subject, predicate: 'is', object: 'chameleon' })

    whenAll: m.predicate == 'eats' && m.object == 'worms' 
    run: assert({ subject: m.subject, predicate: 'is', object: 'bird' })

    whenAll: m.predicate == 'is' && m.object == 'frog'
    run: assert({ subject: m.subject, predicate: 'is', object: 'green' })

    whenAll: m.predicate == 'is' && m.object == 'chameleon'
    run: assert({ subject: m.subject, predicate: 'is', object: 'green' })

    whenAll: m.predicate == 'is' && m.object == 'bird' 
    run: assert({ subject: m.subject, predicate: 'is', object: 'black' })

    whenAll: +m.subject
    run: console.log('fact: ' + m.subject + ' ' + m.predicate + ' ' + m.object)

    whenStart: {
        assert('animal', { subject: 'Kermit', predicate: 'eats', object: 'flies' });
        assert('animal', { subject: 'Kermit', predicate: 'lives', object: 'water' });
        assert('animal', { subject: 'Greedy', predicate: 'eats', object: 'flies' });
        assert('animal', { subject: 'Greedy', predicate: 'lives', object: 'land' });
        assert('animal', { subject: 'Tweety', predicate: 'eats', object: 'worms' });
    }
});

d.runAll();